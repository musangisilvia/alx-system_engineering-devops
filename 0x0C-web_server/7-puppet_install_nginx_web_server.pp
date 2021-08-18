# install and set up nginx

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'add-rewrite':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH@-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
