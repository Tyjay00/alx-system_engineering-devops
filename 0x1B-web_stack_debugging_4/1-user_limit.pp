# Enables user to login in and open files wihtout error.

# Increases the soft file limit for the user Holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/5/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increases the hard file limit for the user Holberton
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
