#Wordpress versions used on Slovak domains (01-apr-2016)

Total domains scanned **301 433**. WordPress detected on **24 355 (8%)** domains. WordPress domains updated to latest version 8788 (36%).

![WordPress versions chart](wordpress_versions.png)

### Jupyter Notebook

[View data processing and visualization notebook online](https://github.com/richard-mihalovic/wordpress-versions-on-slovak-domains/blob/master/notebook/WordpressVersionsNotebook.ipynb).

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
