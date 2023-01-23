#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

void Start();
void GetResults();

int i, j, life, maxrand;
char c;

void Start() {
	i = 0;
	j = 0;
	life = 0;
	maxrand = 6;
	bool z=false;
	
	cout << "ѡ��һ���ʺ�����Ѷ�:\n"; // the user has to select a difficutly level
	cout << "1 : �� (0-15)\n";
	cout << "2 : �е� (0-30)\n";
	cout << "3 : �ǳ��� (0-50)\n";
	cout << "���߼�����һ�����˳�\n";
	c = 30;

	cin >> c;                   // read the user's choice
	cout << "\n";

	switch (c) {
		case '1':
			maxrand = 15;  // the random number will be between 0 and maxrand
			life=5; 
			break;
		case '2':
			maxrand = 30;
			life=6;
			break;
		case '3':
			maxrand = 50;
			life=7;
			break;
		case '#':
			cout<<"--�ѽ����Զ���ģʽ--\n";
			cout<<"�����maxrand=";
			cin>>maxrand;
			cout<<"���Դ���life=";
			cin>>life;
			cout<<"��������j=";
			cin>>j;
			z=true;
			break;
		default:
			exit(0);
		break;
	}
//	life = 5;         // number of lifes of the player
	srand((unsigned)time(NULL)); // init Rand() function
	if(!z){
		j = rand() % maxrand;  // j get a random value between 0 and maxrand
	}
	
	GetResults();
}

void GetResults() {
	if (life <= 0) { // if player has no more life then he loses
		cout << "������ !���������"<<j<<"\n\n";
		cout<<"��Ҫ����,����һ�ְ�(��:1��:������һ����)\n";
		cin>>c;
		switch(c){
			case '1':
				Start();
			default:
				exit(0);
		}
	}

	cout << "����һ������: \n";
	cin >> i;
	
	if((i>maxrand) || (i<0)) { // if the user number isn't correct, restart
		cout << "����: ���ֲ���0��" << maxrand<<"֮�� \n\n";
		GetResults();
	}

	if(i == j) {
		cout << "��Ӯ��!\n\n"; // the user found the secret number
		cout<<"��������һ����?(��:1��:������һ����)\n";
		cin>>c;
		switch(c){
			case '1':
				Start();
			default:
				exit(0);
		}
	} else if(i>j) {
		cout << "̫����\n";
		life = life - 1;
		cout << "ʣ�����: " << life << "\n\n";
		GetResults();
	} else if(i<j) {
		cout << "̫С��\n";
		life = life - 1;
		cout << "ʣ�����: " << life << "\n\n";
		GetResults();
	}
}

int main() {
	cout << "** ��������Ϸ **\n";
	cout << "�����Ϸ��Ŀ���ǲ�һ������\n";
	cout << "�һ����������ǲ���̫����\n";
	cout << "���߸���������ǲ���̫С��\n\n";
	Start();
	return 0;
}
