if $facts['is_virtual']{
    package { 'smartmontools':
        ensure => purged
    }

}else{ 'smartmontools':
    ensure => installed,
}