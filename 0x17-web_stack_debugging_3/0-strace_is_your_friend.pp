# rename the file causing the problem
exec { 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp':
  provider => 'shell',
}
