# set up client ssh config to connect to server without typing password

include 'ssh::client'

class { 'ssh::client': add_default_entry => false}
ssh::client::host_config_entry{ '*':
  passwordputhentication    => no,
  identityfile              => ~/.ssh/holberton,
  sendenv                   => 'LANG LC_*',
  hashknownhosts            => yes,
  gssapiauthentication      => yes,
  gssapidelegatecredentials => no,
}
