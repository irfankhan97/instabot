from trending import get_trending_tag_counts

new = get_trending_tag_counts(tag="love")

if new < 1000:
    print "is not so much trending..just a common tag...#"
elif new < 10000:
    print 'is becoming new trend....'
elif new < 1000000:
    print("tag is flying high on internet")
elif new < 1000000000:
    print "tag is most trending on internet"