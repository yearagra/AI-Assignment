welcome:-
	nl,
	write('COURSE ADVISORY SYSTEM'),
	nl,
	nl,

	retractall(recommend(_)),
	retractall(cse(_)),
	retractall(ece(_)),
	retractall(csam(_)),
	retractall(csd(_)),


	write('Are You Interested In Computer Science?'),nl,
	read(CSE),
	assert(cse(CSE)),
	nl,

	write('Are You Interested In Electronic And Communication?'),nl,
	read(ECE),
	assert(ece(ECE)),
	nl,

	write('Are You Interested In Computer Science And Applied Mathemaics?'),nl,
	read(CSAM),
	assert(csam(CSAM)),
	nl,

	write('Are You Interested In Computer Science And Design?'),nl,
	read(CSD),
	assert(csd(CSD)),
	nl,

	advice(_),
	preferences(List),nl,
	nl,

	(isempty(List)
		->write('SORRY CANNOT MAKE TO RECOMMEND YOU ANY!' ),nl
		;write('ELECTIVES YOU CAN OPT:'),show(List)),
	clear.

/* CSE Course */
advice('Mobile Computing') :- mc,fail.
advice('Security & Privacy') :- sp,fail.
advice('Computer Systems Architecture') :- csa,fail.
advice('Intelligence Theory') :- ilt,fail.
advice('Data Analytics') :- da,fail.
advice('Image Analysis & Machine Learning') :- iaml,fail.

/*ECE Course */
advice('Communication Systems') :- cs,fail.
advice('Signal Processing') :- sgp,fail.
advice('Hardware') :- hw,fail.
advice('Internet of Things') :- it,fail.
advice('Economics') :- eco,fail.
advice('Image Analysis & Machine Learning') :- iml,fail.

/* CSAM Course */
advice('Number Theory ') :- nt,fail.
advice('Advanced Programming ') :- ap,fail.
advice('Signals and Systems') :- ss,fail.
advice('Numerical Methods') :- nm,fail.

/* CSD Course */
advice('Computer Graphics') :- cg,fail.
advice('Data Visualisation') :- dv,fail.
advice('Image Processing') :- ip,fail.
advice('Computer Vision') :- cv,fail.
advice('Machine Learning') :- ml,fail.
advice('Affective Computing') :- ac,fail.
advice('Computer Game Design And Development') :- cgdd,fail.
advice('Animation Priciples And Design') :- apd,fail.
advice('Virtaul Reality') :- vr,fail.


advice('SORRY, NO RECOMMENDATION!').


preferences([Head|Tail]):- retract(recommend(Head)), preferences(Tail).
preferences([]).

show([Head|Tail]):-
	format('~n ~w',[Head]),show(Tail).

show([]).
isempty([]).

/* CSE */
mc :-
	retract(cse(A)),
	assert(cse(A)),
	(A == y
		->true ;fail),
	questioninterest('Do you know java'),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Have you done any hand on project'),
	assert(recommend('Mobile Computing')).

sp :-
	retract(cse(A)),
	assert(cse(A)),
	(A == y
		->true ;fail),
	questioninterest('Do you know python'),
	questioninterest('Do you have good programming skills'),
	questioninterest('Have you done any hand on project'),
        assert(recommend('Security & Privacy')).

csa :-
	retract(cse(A)),
	assert(cse(A)),
        (A == y
		->true ;fail),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Computer Systems Architecture ')).


ilt :-
		retract(cse(A)),
		assert(cse(A)),

		(A == y
			->true ;fail),
		questioninterest('Do you have basic programming skills'),
		assert(recommend('Intelligence Theory')).

da :-
	retract(cse(A)),
	assert(cse(A)),
	( A == y
		->true ;fail),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Do you know basic math'),
	assert(recommend('Data Analytics')).

iaml :-
	retract(cse(A)),
	assert(cse(A)),
	(A == y
		->true ;fail),

	questioninterest('Do you know python'),
	questioninterest('Do you know basic math'),
	assert(recommend('Image Analysis & Machine Learning')).

/* ECE */
cs :-
	retract(ece(B)),
	assert(ece(B)),
	(B == y
		->true ;fail),

	questioninterest('Do you know basic math'),
	assert(recommend('Communication System')).




sgp :-
	retract(ece(B)),
	assert(ece(B)),
	(B == y
		->true ;fail),

	questioninterest('Do you know basic math '),
	assert(recommend('Signal Processing')).


hw :-
	retract(ece(B)),
	assert(ece(B)),
	(B == y
		->true ;fail),
	questioninterest('Do you know basic hardware of PC'),
	assert(recommend('Hardware')).

it :-
	retract(ece(B)),
	assert(ece(B)),

	(B == y
		->true;fail),

	questioninterest('Do you know python'),
	questioninterest('Do you know basic of network'),
	assert(recommend('Internet of Things')).

eco :-
	retract(ece(B)),
	assert(ece(B)),
	( B == y
		->true;fail),

	questioninterest('Do you have interest in economics'),
	assert(recommend('Economics')).

iml :-
	retract(ece(B)),
	assert(ece(B)),
	(B == y
		->true ;fail),

	questioninterest('Do you know python'),
	questioninterest('Do you know basic math'),
	assert(recommend('Image Analysis & Machine Learning')).

/* CSAM */
nt :-
	retract(csam(C)),
	assert(csam(C)),
	(C == y
		->true;fail),
	questioninterest('Do you know basic math'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Number Theory')).

ap :-
	retract(csam(C)),
	assert(csam(C)),
	(C == y
		->true;fail),
	questioninterest('Do you know java'),
	questioninterest('Do you have good programming skills'),
	questioninterest('Have you done any hand on project'),
        assert(recommend('Advanced Programming')).

ss :-
	retract(csam(C)),
	assert(csam(C)),
        (C == y
		->true;fail),
	questioninterest('Do you know basic math'),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Have you done any hand on project'),
	assert(recommend('Signals and Systems')).


nm :-
	retract(csam(C)),
	assert(csam(C)),

	(C == y
		->true;fail),
	questioninterest('Do you know basic math'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Numerical Methods')).

/* CSD */
cg :-
	retract(csd(D)),
	assert(csd(D)),
	( D == y
		->true;fail),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Do you know data structures and algorithm'),
	assert(recommend('Computer Graphics')).

dv :-
	retract(csd(D)),
	assert(csd(D)),
	(D == y
		->true;fail),
	questioninterest('Do you have interest in UI and UX'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Data Visualisation')).

ip :-
	retract(csd(D)),
	assert(csd(D)),
	( D == y
		->true;fail),
	questioninterest('Do you know python '),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Image Processing')).

cv :-
	retract(csd(D)),
	assert(csd(D)),
	(D == y
		->true;fail),
	questioninterest('Do you know python'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Computer Vision')).

ml :-
	retract(csd(D)),
	assert(csd(D)),
	( D == y
		->true;fail),
	questioninterest('Do you know python'),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Do you know basic math'),
	assert(recommend('Machine Learning')).

ac :-
	retract(csd(D)),
	assert(csd(D)),
	(D == y
		->true;fail),

	questioninterest('Do you have basic programming skills'),
	questioninterest('Do you know basic math'),
	assert(recommend('Affective Computing ')).

cgdd :-
	retract(csd(D)),
	assert(csd(D)),
	(D == y
		->true;fail),

	questioninterest('Do you have interest in UI and UX'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Computer Game Design And Development ')).

apd :-
	retract(csd(D)),
	assert(csd(D)),
	( D == y
		->true;fail),
	questioninterest('Do you have interest in animation'),
	questioninterest('Do you have basic programming skills'),
	assert(recommend('Animation Priciples And Design')).

vr :-
	retract(csd(D)),
	assert(csd(D)),
	(D == y
		->true;fail),
	questioninterest('Do you have basic programming skills'),
	questioninterest('Do you know Machine Learning'),
	assert(recommend('Virtaul Reality')).



questioninterest(In) :-
	(yes(In)
		->true
		;(no(In)
			->fail
			;ask(In))).

ask(Que) :-
	format('~w ?',[Que]),
	read(Ans),
	( (Ans == yes ; Ans == y)
		->assert(yes(Que))
		;assert(no(Que)), fail).

:- dynamic yes/1,no/1.


clear :- retract(yes(_)),fail.
clear :- retract(no(_)),fail.
clear.
