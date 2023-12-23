# kill process killmenow

exec {'killmenow':
 path => '/bin/',
 command => 'pkill killmenow',
 onlyif => 'pgrep killmenow',
}
