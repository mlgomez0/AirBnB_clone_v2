#sets up your web servers for the deployment of web_static
exec {'prepare':
  provider => shell,
  command  => 'sudo apt-get update && sudo apt-get install -y nginx && sudo mkdir -p /data/ && sudo mkdir -p /data/web_static/ && sudo mkdir -p /data/web_static/releases/ && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && sudo touch /data/web_static/releases/test/index.html && echo "Hola esta es mi pagina web" | sudo tee /data/web_static/releases/test/index.html && sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current && sudo sed -i "s@server_name localhost;@server_name _;@g" /etc/nginx/sites-enabled/default && sudo sed -i "45 a \ \tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\n\t}" /etc/nginx/sites-enabled/default && sudo service nginx restart',
}
