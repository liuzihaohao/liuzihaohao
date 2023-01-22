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
	
	cout << "选择一个适合你的难度:\n"; // the user has to select a difficutly level
	cout << "1 : 简单 (0-15)\n";
	cout << "2 : 中等 (0-30)\n";
	cout << "3 : 非常难 (0-50)\n";
	cout << "或者键入另一个键退出\n";
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
			cout<<"--已进入自定义模式--\n";
			cout<<"最大数maxrand=";
			cin>>maxrand;
			cout<<"尝试次数life=";
			cin>>life;
			cout<<"秘密数字j=";
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
		cout << "你输了 !这个数字是"<<j<<"\n\n";
		cout<<"不要气馁,再来一局吧(是:1否:键入另一个键)\n";
		cin>>c;
		switch(c){
			case '1':
				Start();
			default:
				exit(0);
		}
	}

	cout << "输入一个数字: \n";
	cin >> i;
	
	if((i>maxrand) || (i<0)) { // if the user number isn't correct, restart
		cout << "错误: 数字不在0和" << maxrand<<"之间 \n\n";
		GetResults();
	}

	if(i == j) {
		cout << "你赢了!\n\n"; // the user found the secret number
		cout<<"还想再来一局吗?(是:1否:键入另一个键)\n";
		cin>>c;
		switch(c){
			case '1':
				Start();
			default:
				exit(0);
		}
	} else if(i>j) {
		cout << "太大了\n";
		life = life - 1;
		cout << "剩余次数: " << life << "\n\n";
		GetResults();
	} else if(i<j) {
		cout << "太小了\n";
		life = life - 1;
		cout << "剩余次数: " << life << "\n\n";
		GetResults();
	}
}

int main() {
	cout << "** 猜数字游戏 **\n";
	cout << "这个游戏的目的是猜一个数字\n";
	cout << "我会告诉你号码是不是太大了\n";
	cout << "或者告诉你号码是不是太小了\n\n";
	Start();
	return 0;
}
