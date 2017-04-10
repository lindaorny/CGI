#!/usr/bin/perl
use CGI qw(:standard);
use POSIX qw(strftime);

sub writeCgiEntry{
   my($logFile) = "message.log";           
   my $date = strftime "%a %b   %e %X %Z %Y", localtime;
   
   # write to log file message.log
   open(LOGFILE, ">>$logFile") or die("Cannot open cgi log file.\n");
   if (param()) {
       my $message = param('message');
       print LOGFILE ("$message\n\n");
       print LOGFILE ("$date\n");
  }
    close(LOGFILE);
}

writeCgiEntry();

# print HTML content including form and submit button
print "Content-type: text/html\n\n";
print "<HTML>";
print "<TITLE>a4q5</TITLE>";
print "<BODY><H1>Message Log</H1>
<FORM method='POST'>
Type message: <input type='text' name='message'><br>
<input type='submit' value='Send Message'></FORM>
<p>Message: </p>";

# print message from getting the data from Logfile
$LOGFILE = "message.log";
open(LOGFILE) or die("Could not open Logfile!");
@lines = reverse (<LOGFILE>);
foreach $line (@lines){
    chomp $line;
    print "<p>$line</p>";
}
print "</BODY>";
print "</HTML>";
