# delete user limits
exec { 'echo "" > /etc/security/limits.conf':
  provider => 'shell',
}
