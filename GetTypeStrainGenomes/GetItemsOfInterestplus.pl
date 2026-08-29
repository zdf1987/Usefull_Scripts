#！c:/Perl64/bin/perl
use strict;
use warnings;
use List::MoreUtils qw/uniq/;
die "\n*************  Something Goes Wrong!!!!  **************\nUsage:\n perl_script genomeList\n\n" unless $ARGV[0];


open (FIL, "<TEM/Species_Numbers.txt") or die "Can't open 'TEM/Species_Numbers.txt': $!";
open (FIL0, "<TEM/specieslinkfile.txt") or die "Can't open 'TEM/specieslinkfile.txt': $!";
my @info1;
foreach my $in (<FIL>) {
	$in=~ s/\n// unless $in=~s/\r\n//;
	next unless $in =~ /\w/;
	$in=~s/-\d\t /\t /;###########个别种名后有‘-1’
	$in=~s/\t\s/\t/;
	push @info1, $in;
}


close FIL;
my $tttt=0;
foreach my $in (<FIL0>) {
	$in=~ s/\n// unless $in=~s/\r\n//;
	next unless $in =~ /\w/;
	my @in=split /\t/, $in;
	if ($info1[$tttt]) {
		$info1[$tttt] .= "	$in[2]";
	} else {
		$info1[$tttt] = "$in[2]";
	}
	
	$tttt++;
}
close FIL0;
my %info;
foreach my $in (@info1) {	
	my @in =split /\t/, $in;
	my @in1 =split /;\s/, $in[1];
	foreach my $ee (@in1) {
##		print "$in $ee\n";
		if ($info{$ee}) {
			$info{$ee} .= "		$in";
		} else {
			$info{$ee} = $in;
		}
	}
}


my (@out1,@out2,@out3);

open (FIL, "<$ARGV[0]") or die "Can't open '$ARGV[0]': $!";
foreach my $in (<FIL>) {
	$in=~ s/\n// unless $in=~s/\r\n//;
	next unless $in;
	my @in =split /\t/, $in;
	print "$in\n" unless $in[7];
	next unless $in[7];
	my $spes= $in[7];	
	
	
	$spes=~ s/\[//;
	$spes=~ s/\]//;	
	my @in1 =split /\s/, $spes;
	my $species = "$in1[0] $in1[1]";
	my $key =$in1[$#in1];
	
	if ($info{$key}) {   #单一菌株号直接匹配
		my @speinfo = split /\t\t/, $info{$key};
		foreach my $s1 (@speinfo) {
			$s1 =~ s/\t\s/\t/;
			my @speinfo1 = split /\t/, $s1;
			my @speinfo2 = split /\s/, $speinfo1[0];
			if ($species =~ /$speinfo1[0]/) {
				push @out1, "$s1	$in\n";
			} elsif ($species =~ /$speinfo2[0]/ || $species =~ /$speinfo2[1]/ ) {  ##只有种名或属名匹配
				push @out2, "$s1	$in\n";
			} else {
				push @out3, "$s1	$in\n";
			}
		}
	}
	$key ="$in1[$#in1-1] $in1[$#in1]"; ##print "$key     AA $info{$key}\n";
	if ($info{$key} ) {   #单一菌株号直接匹配
		my @speinfo = split /\t\t/, $info{$key};
		foreach my $s1 (@speinfo) {
			$s1 =~ s/\t\s/\t/;
			my @speinfo1 = split /\t/, $s1;
			my @speinfo2 = split /\s/, $speinfo1[0];
			if ($species =~ /$speinfo1[0]/) {
				push @out1, "$s1	$in\n";
			} elsif ($species =~ /$speinfo2[0]/ || $species =~ /$speinfo2[1]/ ) {  ##只有种名或属名匹配
				push @out2, "$s1	$in\n";
			} else {
				push @out3, "$s1	$in\n";
			}
		}
		
	}
	
	
	unless ($in[8] eq "na") {
		my $strain =$in[8];
		$strain =~ s/strain=//;
		if ($info{$strain}) {   #单一菌株号直接匹配
			my @speinfo = split /\t\t/, $info{$strain};
			foreach my $s1 (@speinfo) {
				$s1 =~ s/\t\s/\t/;
				my @speinfo1 = split /\t/, $s1;
				my @speinfo2 = split /\s/, $speinfo1[0];
				if ($species =~ /$speinfo1[0]/) {
					push @out1, "$s1	$in\n";
				} elsif ($species =~ /$speinfo2[0]/ || $species =~ /$speinfo2[1]/ ) {  ##只有种名或属名匹配
					push @out2, "$s1	$in\n";
				} else {
					push @out3, "$s1	$in\n";
				}
			}
		}
	}
	next if $in[9] eq "na";
	if ($info{$in[9]}) {   #单一菌株号直接匹配
		my @speinfo = split /\t\t/, $info{$in[9]};
		foreach my $s1 (@speinfo) {
			$s1 =~ s/\t\s/\t/;
			my @speinfo1 = split /\t/, $s1;
			my @speinfo2 = split /\s/, $speinfo1[0];
			if ($species =~ /$speinfo1[0]/) {
				push @out1, "$s1	$in\n";
			} elsif ($species =~ /$speinfo2[0]/ || $species =~ /$speinfo2[1]/ ) {  ##只有种名或属名匹配
				push @out2, "$s1	$in\n";
			} else {
				push @out3, "$s1	$in\n";
			}
		}
	}

	
}
close FIL;


@out1 = uniq @out1;#print "AAAAA @out1\n";
@out2 = uniq @out2;
@out3 = uniq @out3;
@out2=sort @out2;
@out3=sort @out3;
my (%outL,%outL2,%outLen,@out1s,@gca);
push @gca, "1";
foreach my $uni (sort @out1) {

	my @in =split /\t/, $uni;
	if ($outL2{$in[20]}) {
		$outL2{$in[20]}= $uni if $uni =~ /correct name/;######????   这句话写的好像没啥用
	} else {
		$outL2{$in[20]}= $uni;
	}
}	
my @rr = keys %outL2;



#foreach my $uni (@rr) {	
#	my @in =split /\t/, $outL2{$uni};
#	if ($outL{$in[0]}) {
#		$outL{$in[0]}=$outL2{$uni} if $in[33] < $outLen{$in[0]};
#		$outLen{$in[0]}=$in[33] if $in[33] < $outLen{$in[0]};

#	} else {
#		$outL{$in[0]}=$outL2{$uni};
#		$outLen{$in[0]}=$in[33];

#	}
#}
#my @rt = keys %outL;                  这一部分不执行确保同一个种名对应的多个基因组都能输出




my @rt = sort keys %outL2;   #####################    @gca没有使用

open (OU, ">TypeStrainGenomeInfo.txt") or die "Can't open '$ARGV[0].txt': $!";
print OU  "Perfect matches:\n";
foreach my $uni (@rt) {
	my @in =split /\t/, $outL2{$uni};  ####$outL{$uni}
	push @gca, $in[20];
	print OU "$outL2{$uni}";    ####$outL{$uni}
}

print OU  "\n\n\n\n\nGood matches (Sharing genus or specific name):\n";

foreach my $uni (0..$#out2) {
	my @in =split /\t/, $out2[$uni];
	next if $in[21] ~~ @gca;
	push @gca, $in[20];
	print OU "$out2[$uni]" unless $outL{$in[0]};
}
print OU  "\n\n\n\n\nPossible matches (Only sharing strain number):\n";
foreach my $uni (0..$#out3) {
	my @in =split /\t/, $out3[$uni];
	
	next if $in[21] ~~ @gca;
	push @gca, $in[20];
	print OU "$out3[$uni]" unless $outL{$in[0]};
}

close OU;
	
	
