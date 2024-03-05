# Install nginx web server
exec { 'apt update':
  provider => 'shell'
}
package { 'nginx':
  ensure => installed
}
file { '/var/www/html/index.html':
  content => 'Hello World!'
}
file_line { '301 redirect':
  path  => '/etc/nginx/sites-available/default',
  after => 'listen 80 default_server;',
  line  => "\trewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"
}
exec { 'service nginx restart':
  provider => 'shell'
}
