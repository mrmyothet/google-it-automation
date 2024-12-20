# Idempotent - An action can be performed repeatedly without changing the system after the first run
# "Test and Repair" paradigm - should only take actions when testing determines that need to be done to reach the requested state

class idempotent {
  file { '/etc/issue':
    mode => '0644', 
    content => "Internal system \l \n",
  }

  exec { 'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop', 
    onlyif => 'test -e /home/user/example.txt',
  }
}
