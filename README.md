##Wordpress versions used on Slovak domains

**301 548** Slovak domains scanned, WordPress was detected on **24 215** domains which is about **8%** of all scanned domains.

![WordPress versions chart](wordpress_versions.png)

### Requirements
Python 2.7 installed  
Scrapy (for collecting data)  
Jupyter Notebook (for data processing and visualization)

### Collect data
```
pip install scrapy
./grab_data.sh
```

### Visualize data
```
pip install jupyter
jupyter-notebook notebook/WordpressVersionsNotebook.ipynb
```
