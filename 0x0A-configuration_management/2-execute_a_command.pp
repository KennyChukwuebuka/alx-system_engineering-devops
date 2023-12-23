# kill process killmenow

exec {'killmenow':
 path => '/bin:/usr/bin',
 command => 'pkill killmenow',
 onlyif => 'pgrep killmenow',
}
