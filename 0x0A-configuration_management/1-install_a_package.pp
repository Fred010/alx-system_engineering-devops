# install_flask.pp

package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
}
