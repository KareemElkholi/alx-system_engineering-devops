# kills a process named killmenow
exec { 'pkill killmenow':
  provider => 'shell',
}
