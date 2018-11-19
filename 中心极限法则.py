import numpy as np
import matplotlib as plt

samples = []
samples_mean = []
samples_std = []

random_data = np.random.randint(1, 7, 10000)
for i in range(0, 1000):
    sample = []
    for j in range(0, 50):
        sample.append(random_data[int(np.random.random() * len(random_data))])
    sample_np = np.array(sample)
    samples_mean.append(sample_np.mean())
    samples_std.append(sample_np.std())
    samples.append(sample_np)

samples_mean_np = np.array(samples_mean)
samples_std_np = np.array(samples_std)

print(samples_mean_np)

plt.figure()
samples_mean_np.hist()
plt.show()

