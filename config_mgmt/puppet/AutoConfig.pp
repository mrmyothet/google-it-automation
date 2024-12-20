class AutoConfig {
    package { 'Executable':
        ensure => latest,
    }

    file { 'executable.cfg':
        source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
        replace => true,
    }

    service { 'executable.ext'
        enable => true, 
        ensure => running,
    }
}