# install and add custom header to nginx

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  require => Package['nginx'],
  content => 'Holberton School',
}

file_line { 'add_header':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  notify  =>  Service['nginx'],
}

service { 'nginx':
  ensure  => running
  require => File_line['add_header'],
}
