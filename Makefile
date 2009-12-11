cdn:
	# Push media to amazon
	sh -c '(cd media ; s3cmd sync  -M --acl-public markitup-1.1.5 s3://s.hdimg.net/)'