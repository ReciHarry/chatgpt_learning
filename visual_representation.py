import matplotlib.pyplot as plt
import numpy as np

# Exploration of Linear Increase:
# Construct an adaptable graphical representation that delineates the progression of a value starting from 1, undergoing a consistent 1% linear increment across varying iterations.

def linear_increase(scale):
    n = float(1)
    values = [n]
    for i in range(1, scale):
        n = n * 1.01
        values.append(n)
    
    return values

scale = 365
values = linear_increase(scale)

# Creating a figure with a subplot layout: 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plotting the main graph
ax1.plot(range(1, scale+1), values)
ax1.set_xlabel("Number of Increases")
ax1.set_ylabel("Value")
ax1.set_title("Linear Increase by 1%")

# Calculating step size to achieve approximately 10 labels
step_size = max(1, len(values) // 10)

# Creating a list of labels for the graph
for i, value in enumerate(values):
    if i == 0 or i == scale - 1 or i % step_size == 0:
        ax1.text(i + 1, value + 0.03, f'{i+1}', ha='center', va='top')

# Creating a list of labels and values for the side panel
label_list = [f'{i+1}: {value:.2f}' for i, value in enumerate(values) if i == 0 or i == scale - 1 or i % step_size == 0]

# Displaying the list of labels and values on the side panel
ax2.axis('off')
ax2.text(0, 0.5, '\n'.join(label_list), va='center')

plt.tight_layout()
plt.show()

# Analysis of Increasing Compound Interest:
# Construct an adjustable graph that portrays the augmenting compounding interest arising from an initial value of 1, demonstrating cumulative growth over multiple compounding cycles.

def compound_interest_graph(initial_value, interest_rates):
    values = [initial_value]
    
    for rate in interest_rates:
        initial_value *= (1 + rate)
        values.append(initial_value)
    
    return values

initial_value = 1
mean_interest = 0.02
std_dev_interest = 0.03

compounding_periods = 150
interest_rate = [round(max(0.01, min(0.15, np.random.normal(mean_interest, std_dev_interest))), 2)
                 for _ in range(compounding_periods)]

values = compound_interest_graph(initial_value, interest_rate)

plt.plot(range(compounding_periods + 1), values)
plt.xlabel("Compounding Periods")
plt.ylabel("Accumulated Amount")
plt.title("Compound Interest Growth with Random Interest Rates (Line Graph)")
plt.show()

# Examination of Decreasing Compound Interest:
# Develop a flexible graphical visualization that elucidates the diminishing compounding interest effectuated by an initial value of 1 by 1%, revealing the attenuation over successive compounding intervals.

def linear_decrease(scale):
    n = float(1)
    values = [n]
    for i in range(1, scale):
        n = n * 0.99
        values.append(n)
    
    return values

scale = 365
values = linear_decrease(scale)

# Creating a figure with a subplot layout: 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plotting the main graph
ax1.plot(range(1, scale+1), values)
ax1.set_xlabel("Number of Decreases")
ax1.set_ylabel("Value")
ax1.set_title("Linear Decrease by 1%")

# Calculating step size to achieve approximately 10 labels
step_size = max(1, len(values) // 10)

# Creating a list of labels for the graph
for i, value in enumerate(values):
    if i == 0 or i == scale - 1 or i % step_size == 0:
        ax1.text(i + 1, value + 0.03, f'{i+1}', ha='center', va='top')

# Creating a list of labels and values for the side panel
label_list = [f'{i+1}: {value:.2f}' for i, value in enumerate(values) if i == 0 or i == scale - 1 or i % step_size == 0]

# Displaying the list of labels and values on the side panel
ax2.axis('off')
ax2.text(0, 0.5, '\n'.join(label_list), va='center')

plt.tight_layout()
plt.show()

# Visualizing Combined Trends of Linear Growth and Compounding Interest:
# Create a graphical representation that combines increasing and decreasing compound interest curves, providing a holistic view of their simultaneous behaviors.

def compound_interest_graph(initial_value, growth_rate, periods):
    values = [initial_value]
    
    for _ in range(periods):
        initial_value *= growth_rate
        values.append(initial_value)
    
    return values

initial_value = 1
periods = 365  

decreasing_values = compound_interest_graph(initial_value, 0.99, periods)
increasing_values = compound_interest_graph(initial_value, 1.01, periods)

plt.plot(range(periods + 1), decreasing_values, label="Decreasing by 1%")
plt.plot(range(periods + 1), increasing_values, label="Increasing by 1%")
plt.xlabel("Periods")
plt.ylabel("Accumulated Amount")
plt.title("Linear Compound Interest Growth")
plt.legend()

plt.annotate(f"Start: {decreasing_values[0]:.2f}", (0, decreasing_values[0]), textcoords="offset points", xytext=(0,0), ha='center')
plt.annotate(f"End: {decreasing_values[-1]:.2f}", (periods, decreasing_values[-1]), textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate(f"End: {increasing_values[-1]:.2f}", (periods, increasing_values[-1]), textcoords="offset points", xytext=(10,10), ha='center')

plt.show()

# Integration of Perturbed Values:
# Extending the preceding graph, introduce randomized values that introduce perturbations capable of influencing the graph's trajectory, while retaining the underlying directional tendencies.

# Function to generate data with random spikes
def generate_data_with_spikes(initial_value, growth_rate, periods, spike_prob=0.05, spike_amplitude_range=(0.2, 0.5), spike_direction_prob=0.5):
    values = [initial_value]
    
    for _ in range(periods):
        # Determine if a spike occurs
        spike = np.random.rand() < spike_prob
        
        # Determine the amplitude and direction of the spike
        spike_amplitude = np.random.uniform(*spike_amplitude_range)
        spike_direction = np.random.rand() < spike_direction_prob
        spike_multiplier = (1 + spike_amplitude) if spike_direction else (1 - spike_amplitude)
        
        # Apply the spike or normal growth
        initial_value *= (spike_multiplier if spike else growth_rate)
        values.append(initial_value)
    
    return values

# Function to smooth data using a moving average
def smooth_data(data, window_size=15):
    return [np.mean(data[max(0, i - window_size // 2):min(len(data), i + window_size // 2 + 1)]) for i in range(len(data))]

initial_value = 1
periods = 125

# Generate data with spikes
decreasing_values_with_spikes = generate_data_with_spikes(initial_value, 0.99, periods, spike_direction_prob=0.3)
increasing_values_with_spikes = generate_data_with_spikes(initial_value, 1.01, periods, spike_direction_prob=0.7)

# Smooth the generated data
smoothed_decreasing_values = smooth_data(decreasing_values_with_spikes)
smoothed_increasing_values = smooth_data(increasing_values_with_spikes)

plt.plot(range(periods + 1), smoothed_decreasing_values, label="Decreasing by 1% (Smoothed)")
plt.plot(range(periods + 1), smoothed_increasing_values, label="Increasing by 1% (Smoothed)")
plt.xlabel("Periods")
plt.ylabel("Accumulated Amount")
plt.title("Smoothed Linear Compound Interest Growth with Random Spikes")
plt.legend()

plt.annotate(f"Start: {decreasing_values_with_spikes[0]:.2f}", (0, decreasing_values_with_spikes[0]), textcoords="offset points", xytext=(0,0), ha='center')
plt.annotate(f"End: {decreasing_values_with_spikes[-1]:.2f}", (periods, decreasing_values_with_spikes[-1]), textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate(f"End: {increasing_values_with_spikes[-1]:.2f}", (periods, increasing_values_with_spikes[-1]), textcoords="offset points", xytext=(-20,-10), ha='center')

plt.show()