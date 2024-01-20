# kill_process.pp

exec { 'pkill':
  command     => 'pkill killmenow',
  provider        => 'shell',
}
