import numpy as np

# --- 1. Generate Fibonacci envelope ------------------------
def fib(n=30):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return np.asarray(seq, dtype=float)

drive = fib(60)
drive /= drive.max()          # normalise 0‒1 for coil DAC

# --- 2. Model cross-talk as delayed echo -------------------
def echo(signal, delay=5, gain=0.7):
    """Return signal + delayed duplicate (simple FIR model)."""
    tap = np.zeros(delay + 1)
    tap[0] = 1.0              # direct path
    tap[-1] = gain            # echo path
    return np.convolve(signal, tap, mode="same")

sensor = echo(drive, delay=5, gain=0.7)

# --- 3. Display numeric evidence ---------------------------
print("Step | Coil drive | Sensor reading")
print("-------------------------------")
for k, (d, s) in enumerate(zip(drive, sensor)):
    flag = " ← echo" if abs(s - d) > 1e-9 else ""
    print(f"{k:>4} | {d:8.18f}   | {s:8.18f}{flag}")
