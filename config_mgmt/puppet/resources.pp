class sudo {
    package { 'sudo':
    ensure => present,
    }
}

class sysctl {
    file {'etc/sysctl.d':
        ensure => directory,
    }
}

class timezone {
    file { '/etc/timezone':
        ensure => file, 
        content => "UTC\n",
        replace => true,
    }

}