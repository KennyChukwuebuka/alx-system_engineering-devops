# Custom HTTP header in a nginx server

# this is to update ubuntu server
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# this is to install nginx web server on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# write the custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# this is to start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}