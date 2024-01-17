# Puppet File Line Replacement Script

This Puppet script is designed to replace a specific line in a file on a server. The `file_to_edit` variable specifies the file to be modified.

## Usage

1. Set the `file_to_edit` variable in the script to the path of the file you want to modify.

    ```puppet
    $file_to_edit = '/var/www/html/wp-settings.php'
    ```

2. Run the Puppet script to execute the line replacement.

    ```bash
    puppet apply your_script.pp
    ```

## Script Details

The script utilizes the Puppet `exec` resource to execute a `sed` command. The `sed` command replaces the string "phpp" with "php" in the specified file.

```puppet
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin'],
}
