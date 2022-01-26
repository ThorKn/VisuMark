# VisuMark
Visualize benchmark results. A framework in flask, dash and plotly.

### Usage
From inside the webapp-folder export the FLASK_APP variable and run flask with
```
export FLASK_APP="__init__"
run flask
```

When uploaded to a webserver it is a little more work to do.
The next steps may vary depending on your production evironment.
Our webserver is an Apache2 and the deployment method
for the flask application is the mod_wsgi module running with the Apache.

Rough idea:

1. Enable mod_wsgi in Apache2.

2. Give some Directives to the Apache to find the wsgi script, the python
environment, the python packages and enable the directories for python execution.

3. Upload everything to webspace.

4. Send some prayers to the interwebz to make it work.
