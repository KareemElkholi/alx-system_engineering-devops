# ULIMIT increase
exec { 'echo "ULIMIT=\"-n 4096\"" > /etc/default/nginx && service nginx restart':
  provider => 'shell',
}
