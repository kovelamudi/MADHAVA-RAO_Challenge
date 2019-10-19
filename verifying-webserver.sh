url="http://ec2-54-174-75-227.compute-1.amazonaws.com"
content="$(curl -sLI "$url" | grep HTTP/1.1 | tail -1 | awk {'print $2'})"
if [ ! -z $content ] && [ $content -eq 200 ]
then
echo "Webserver is up"
else
echo "webserver is down"
fi
