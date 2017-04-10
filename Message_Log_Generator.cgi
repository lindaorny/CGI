# !/usr/bin/perl
# use CGI qw/:standard/;
#
# sub writeCgiEntry{
#   my($logFile) = "message.log";
#   my($datestring) = localtime();
#
#   open(LOGFILE, ">>$logFile") or die("Cannot open cgi log file.\n");
#   print LOGFILE ("$datestring\n");
#   if (param()) {
#       my $message = param('message');
#       print LOGFILE ("$message\n\n");
#   }
#    close(LOGFILE);
# }
#
# writeCgiEntry();
#
# print "Content-type: text/html\n\n";
# print "<HTML>";
# print "<TITLE>a4q5</TITLE>";
# print "<BODY><H1>Message Log</H1>
# <FORM method='GET' onSubmit='writeCgiEntry();'>
# Type message: <input type='text' name='message'><br>
# <input type='submit' value='Send Message'></FORM>
# <p>Message: </p></BODY>";
# print "</HTML>";
