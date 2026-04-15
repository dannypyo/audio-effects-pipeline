from functools import partial, reduce


# Audio Effects
# Adjust volume by a percentage
def adjust_volume(percent):
    return lambda signal: [x * percent for x in signal]

# Adds a copy of the rest of the array after the delay and reduces volume by half
def add_echo(delay):
    def effect(signal):
        newSignal = signal[:]
        for i in range(delay, len(signal)):
            newSignal.append(signal[i]*.5)
        return newSignal
    return effect

# Creates a threshold (maximum and minimum) and sets any value above or below to that value
def distort(threshold):
    return lambda signal: [
        max(min(x, threshold), -threshold) for x in signal
    ]


# Compose Function
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


# Simulated Audio Signal
audio_signal = [0.2, 0.5, -0.4, 0.7, -0.8, 0.3]


# Create Curried Effects
volume = adjust_volume(0.8)
echo = add_echo(3)
clipping = distort(0.6)


# Compose Effects Pipeline
audio_pipeline = compose(clipping, echo, volume)

# Apply pipeline
processed_audio = audio_pipeline(audio_signal)

print("Original:", audio_signal)
print("Processed:", processed_audio)
