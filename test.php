<html>
<meta http-equiv="Content-Type" content="text/html;
charset=UTF-8" />
<body>
<?php
$input1=(htmlspecialchars($_POST['input1'],ENT_QUOTES));
$input2=(htmlspecialchars($_POST['input2'],ENT_QUOTES));
print ($input1.'</br>');
print ($input2.'</br>');

$titlefile = fopen("text/title.txt", "w") or die("Unable to open file!");
$txt = $input1;
fwrite($titlefile, $txt);
fclose($titlefile);

$textfile = fopen("text/text.txt", "w") or die("Unable to open file!");
$txt = $input2;
fwrite($textfile, $txt);
fclose($textfile);

$command="export GOOGLE_APPLICATION_CREDENTIALS=key/sentiment-255007-d2422bce635d.json"
exec($command);

$command="python sentiment.py text/title.txt";
exec($command,$output);
print "$output\n";

$command="python sentiment.py text/text.txt";
exec($command,$output);
print "$output\n";
?>
</body>
</html>