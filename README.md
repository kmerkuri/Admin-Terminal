# Admin-Terminal

Installing required dependencies.

apt-get update -y
apt-get install -y python python-dev redis-server python-pip supervisor
apt-get install software-properties-common build-essential libpulse-dev libssh-dev libwebp-dev libvncserver-dev software-properties-common curl gcc libavcodec-dev libavutil-dev libcairo2-dev libswscale-dev libpango1.0-dev libfreerdp-dev libssh2-1-dev libossp-uuid-dev jq wget libvorbis-dev libtelnet-dev libssl-dev libjpeg-dev libjpeg-turbo8-dev -y 

Installing Apache Guacamole
apt install -y  gcc-6 g++-6 libcairo2-dev libjpeg-turbo8-dev libpng-dev \
libossp-uuid-dev libavcodec-dev libavutil-dev libswscale-dev libfreerdp-dev \
libpango1.0-dev libssh2-1-dev libvncserver-dev libssl-dev libvorbis-dev libwebp-dev

apt install tomcat8 tomcat8-admin tomcat8-common tomcat8-user -y

cd /tmp

wget https://sourceforge.net/projects/guacamole/files/current/source/guacamole-server-0.9.14.tar.gz
tar xzf guacamole-server-0.9.14.tar.gz 
cd guacamole-server-0.9.14
./configure --with-init-dir=/etc/init.d
make CC=gcc-6
make install
ldconfig
systemctl enable guacd
systemctl start guacd

For more in Apache Guacamole follow the link.
https://kifarunix.com/how-to-setup-guacamole-web-based-remote-desktop-access-tool-on-ubuntu-18-04/


Web Terminal install.

git clone https://github.com/kmerkuri/Admin-Terminal.git
cd webterminal
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py host:port



Copyrighting https://github.com/jimmy201602/webterminal.git
