# *latenZy* — Preprocessing Guidlines 

## Preparing trial-aligned data for ***`latenZy`***
***`latenZy`*** requires spike and event times as continuous, absolute (global) timestamps. If your data is trial-aligned (e.g., spikes relative to stimulus onset) and you don't have the original event times, you can simulate them by assigning large, fixed offsets between repetitions (e.g., 100s apart):

**Python example:**
```python
import numpy as np

# Trial-aligned spike times for 5 trials (relative to stimulus onset)
aligned_spikes = [
    [-0.3, 0.2, 0.3 0.7],
    [-0.4, 0.1, 0.5],
    [-0.6, -0.1, 0.3 0.6],
    [-0.2, 0.1 0.4, 0.9],
    [-0.5, 0.6]
]

# Simulated absolute event (stimulus) times, spaced 100s apart
event_times = np.arange(100, 100 * len(aligned_spikes) + 1, 100)

# Offset each trial's spikes by its simulated global event time
new_spikes = []
for i, t_event in enumerate(event_times):
    new_spikes.append(np.array(aligned_spikes[i]) + t_event)

# Flatten all spikes into a global spike time array
spike_times = np.concatenate(new_spikes)
```

**MATLAB example:**
```matlab
alignedSpikes = {
    [-0.3, 0.2, 0.3, 0.7];
    [-0.4, 0.1, 0.5];
    [-0.6, -0.1, 0.3, 0.6];
    [-0.2, 0.1, 0.4, 0.9];
    [-0.5, 0.6]
};

% Simulated absolute event (stimulus) times, spaced 100s apart
eventTimes = 100:100:(100 * numel(alignedSpikes));

% Offset each trial's spikes by its simulated global event time
newSpikes = cell(size(alignedSpikes));
for i = 1:numel(alignedSpikes)
    newSpikes{i} = alignedSpikes{i} + eventTimes(i);
end

% Flatten all spikes into a global spike time array
spikeTimes = [newSpikes{:}];
```

This produces pseudo-global spike and event times compatible with *`latenZy`*. In the first step of the algorithm, data is stitched across repetitions by removing spikes outside the event window `use_dur`/`useDur`. The excluded intervals between event repetiations are substracted from all subsequent times, creating a continuous timeline of only event-related activity for statistics.
> ⚠️ **Important:** Make sure `use_dur`/`useDur` does **not** include periods without spikes, as silent intervals distort the stitched data and bias latency estimates.



