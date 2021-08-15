# set up client ssh config to connect to server without typing password

class { 'ssh::client':
  options => {
    'Host *' => {
      'PasswordAuthentication'    => 'no',
      'IdentityFile'              => '~/.ssh/holberton',
      'SendEnv'                   => 'LANG LC_*'
      'HashKnownHosts'            => 'yes'
      'GSSAPIAuthentication'      => 'yes'
      'GSSAPIDelegateCredentials' => 'no'
    },
  },
}
