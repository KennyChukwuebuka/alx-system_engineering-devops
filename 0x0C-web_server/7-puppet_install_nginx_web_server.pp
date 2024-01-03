# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define Nginx server block
file { '/etc/nginx/sites-available/redirect_config':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name _;

      root /var/www/html;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 https://google.com/new_page;
      }

      error_page 404 /404.html;
      location = /404.html {
        root /var/www/html;
        return 404 'Ceci n\'est pas une page';
      }
    }
  ",
  require => Package['nginx'],
}

# Enable the server block by creating a symbolic link
file { '/etc/nginx/sites-enabled/redirect_config':
  ensure  => link,
  target  => '/etc/nginx/sites-available/redirect_config',
  require => File['/etc/nginx/sites-available/redirect_config'],
  notify  => Service['nginx'],
}

# Create directories for web content
file { '/var/www/html':
  ensure => directory,
}

# Reload Nginx after making changes
exec { 'reload_nginx':
  command     => 'systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-enabled/redirect_config'],
}

