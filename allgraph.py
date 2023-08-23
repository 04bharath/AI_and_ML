# Scatter chart
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/tips.csv")
plt.scatter(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('Tip')
plt.show()

# Line Chart
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/tips.csv")
plt.plot(data['tip'])
plt.plot(data['size'])
plt.xlabel('day')
plt.ylabel('Tip and size')
plt.show()

# Bar chart
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/tips.csv")
plt.bar(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('Tip')
plt.title('Bar chart')
plt.show()

# Histrogram chart
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/tips.csv")
plt.hist(data['total_bill'])

