# install and set up nginx

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  require => Package['nginx'],
  content => 'Holberton School',
}

file_line { 'add-rewrite':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH@-TGUlwu4 permanent;',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['add-rewrite'],
}
