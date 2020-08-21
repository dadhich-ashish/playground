# Tomcat + Angular2 404 Issue Fix

This configuration is needed when we're deploying angular application on tomcat application server.
This is with the Angular2+ while deploying application on tomcat and try to access deeplinks from the browser directly will throw a 404 error.

# Solution
Follow below steps to fix the issue 
- Configure the RewriteValve in server.xml
- Write the rewrite rule in rewrite.config
- Restart server :) 

### Configure the RewriteValve in server.xml
Update the server.xml file in `apache-tomcat-x.x.xx\conf` folder
```
<Host name="localhost"  appBase="webapps" unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />
		<Valve className="org.apache.catalina.valves.rewrite.RewriteValve" />
</Host>
```
### Write the rewrite rule in rewrite.config
Create file in `apache-tomcat-x.x.xx\conf\Catalina\localhost` folder, and add content 
```
RewriteCond %{REQUEST_PATH} !-f
RewriteRule ^/rit/(.*) /rit/index.html
```