# osr2png - rewrite³

This repository is forked version of [osr2png](https://github.com/xjunko/osr2png), added GUI by me.

osr2png is a  thumbnail generator for osu! maps.

## Styles

## Style 1
![image](https://github.com/xjunko/osr2png/assets/44401509/98f06ad3-edf7-4998-a853-c4ed24941af3)
![image](https://github.com/xjunko/osr2png/assets/44401509/463729ef-d474-445a-93b1-d08824727f59)

## Style 2
![image](https://github.com/xjunko/osr2png/assets/44401509/d6066692-1c27-4356-b7f9-58b19b4b5e20)
![image](https://github.com/xjunko/osr2png/assets/44401509/8b548487-4ccd-4ba4-b7b4-10e700189878)


## Running
- 먼저, osu! 홈페이지에 로그인하고, [여기](https://osu.ppy.sh/home/account/edit)에 접속합니다.
- OAuth 탭에 `새 OAuth 애플리케이션`을 눌러 OAuth 클라이언트를 생성합니다. 본인 소유의 클라이언트가 있다면 건너뛰어도 됩니다.
- OAuth 클라이언트 ID와 Secret을 복사해서, 다음 형식의 `apikey.txt`를 생성합니다.
```
<OAuth ID>
<OAuth Secret>
```
- [Pre-release](https://github.com/Unlimitosu/osr2png-gui/releases/tag/pre-release)에서 .exe 파일을 다운로드 받습니다.
- 사용할 폴더 안에 .exe 파일과 `apikey.txt`를 넣고 실행합니다.
- Replay를 선택하고 Run을 누르면 output 폴더가 생기며, replay 파일명과 동일한 썸네일이 생성됩니다.
- Save Preset 버튼을 누르면 현재 설정이 preset.txt 파일에 저장되며, 이후 osr2png를 실행하면 동일한 설정이 적용됩니다.

## FAQ
- Style 2에서 최대 콤보가 0으로 나옵니다.
  - 버그입니다. 수정할 예정입니다.

- pp 값이 실제와 다릅니다.
  - 버그입니다. 원작자 코드에서도 동일한 듯 합니다.

- .exe를 실행했는데 터미널 창이 나왔다가 바로 꺼집니다.
  - `apikey.txt`를 같은 폴더 내에 두었는지 확인해보세요.

- height, width 등의 값을 수정하고 Run을 누르니까 강제종료됩니다.
  - 입력 허용 범위 밖의 값입니다. 되도록이면 기본 값을 사용하세요.


## Credits

- [rosu-pp](https://github.com/MaxOhn/rosu-pp): The PP calculator used in this program.
- [kitsu.moe](https://kitsu.moe/): The mirror that is used for getting the beatmap
  data.
