# using puppet to make changes to config file advance task

file_line { 'Turn off passwd auth':
 ensure =>  'present',
 path   =>  '/etc/ssh/ssh_config',
 line   =>  'PasswordAuthentication no',
}
file_line { 'Declare file':
 ensure =>  'present',
 path   =>  '/etc/ssh/ssh_config',
 line   =>  'IdentityFile ~/.ssh/school',
}
