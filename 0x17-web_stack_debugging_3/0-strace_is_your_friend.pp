# This Puppet script replaces a line in a file on a server.
# The `file_to_edit` variable specifies the file to edit.

$file_to_edit = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
