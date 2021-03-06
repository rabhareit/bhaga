from slackbot.bot import respond_to, default_reply
from plugins.gomisute.SQLRepository import getCount, getMentionCount, countMention

import datetime

count = 0

fire_spaghetti = """
\t:fire::fire::fire:
\t:fire::spaghetti::fire:
\t:fire::fire::fire:
"""

ring_Iine = """
\t\t\t\t:+1:
\t\t:+1:\t\t\t:+1:
:+1:\t\t\t\t\t\t\t:+1:
\t\t:+1:\t\t\t:+1:
\t\t\t\t:+1:
"""

@respond_to(r'^cd\s.*')
def cdReply(message, *args):
    message.reply('チャンネルの変更ですか？画面左のメニューバーからどうぞ。')

@respond_to(r'^ls(\s.*)+')
def lsReply(message, *args):
    message.reply('ダウンロードファイルの一覧ですか？画面右上のボタンからどうぞ。')

@respond_to(r'^mv\s.*\s.*')
def mvReply(message, *args):
    message.reply('ファイルの移動は手動でお願いします。')

@respond_to(r'^cp\s.*\s.*')
def cpReply(message, *args):
    message.reply('ファイルのコピーは手動でお願いします。')

@respond_to('clear')
def clearReply(message, *args):
    message.reply('すみません…それはできかねます…。')

@respond_to(r'^mkdir\s.*')
def mkdirReply(message, *args):
    message.reply('ワークスペースディレクトリのことでしょうか？画面右上のボタンからどうぞ。')

@respond_to(r'touch\s.*')
def touchReply(message, *args):
    message.reply('ファイルを追加するにはメッセージフィールドの横にあるペーパークリップアイコンをクリックしてください。')

@respond_to(r'rmdir\s.*')
def rmdirReply(message, *args):
    message.reply('')

@respond_to(r'^rm\s.*')
def mvReply(message, *args):
    message.reply('ファイルの削除は手動でお願いします…。')

@respond_to(r'^rm\s-rf/')
def mvReply(message, *args):
    message.reply('それだけはやめてください...。')

@respond_to(r'pwd')
def pwdReply(message, *args):
    message.reply('shift_botです')

@respond_to(r'find\s/\s\-.*\s.*')
def pwdReply(message, *args):
    message.reply('ファイルビューアからどうぞ。')

@respond_to(r'cat\s.*')
def pwdReply(message, *args):
    message.reply('ファイルビューアをご利用ください…。')

@respond_to(r'diff\s.*\s.*')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'grep\s.*')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'chmod\s[0-9]^3\s.*')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'chown')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'history')
def pwdReply(message, *args):
    message.reply('私の認識が正しければ表示されているはずなのですが…')

@respond_to(r'ln')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'man')
def pwdReply(message, *args):
    message.reply('こちらをどうぞ。\nhttps://slack.com/intl/ja-jp/help/categories/200111606')

@respond_to(r'apropos')
def pwdReply(message, *args):
    message.reply('こちらのページに検索ボタンがありますのでそちらをご利用ください。\nhttps://slack.com/intl/ja-jp/help/categories/200111606')

@respond_to(r'less\s.*')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'more\s.*')
def pwdReply(message, *args):
    message.reply('')


@respond_to(r'(adduser|useradd)\s.*')
def userReply(message, *args):
    message.reply('おや、新入生ですか？')

@respond_to(r'(deluser)\s.*')
def userReply(message, *args):
    message.reply('そういったことは管理者ユーザーが行いますので…')

@respond_to(r'groupadd\s.*')
def pwdReply(message, *args):
    message.reply('チャンネルの追加でしたら画面左のメニューバーからできますよ。')

@respond_to(r'groupdel\s/*')
def pwdReply(message, *args):
    message.reply('チャンネルの削除でしたら画面左のメニューバーからできますよ。')

@respond_to(r'chfn')
def pwdReply(message, *args):
    message.reply('情報を見たいアカウントのプロフィール画像をクリックしてみてください。')


@respond_to(r'free')
def pwdReply(message, *args):
    message.reply('私にはわかりません…。')

@respond_to(r'last')
def pwdReply(message, *args):
    message.reply('すみません、誰が最後までかはわかりません…。')

@respond_to(r'finger')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'^who\s.*')
def whoReply(message, *args):
    message.reply('画面左のメニューバーから見れます。')


@respond_to(r'route')
def pwdReply(message, *args):
    message.reply('')

@respond_to(r'fpt')
def pwdReply(message, *args):
    message.reply('そんなことをしなくてもダイレクトメッセージで送信できますよ。')

@respond_to(r'ssh\s[a-z0-9]*@+\d+\.\d+\.\d+\.\d+\s*$')
def pwdReply(message, *args):
    message.reply('残念ながら私にはできません…。')

@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
def pingReply(message, *args):
    message.reply('それはpingのコマンドですね。実行できませんが。')


@respond_to(r'^passwd\s.*')
def passwdReply(message, *args):
    message.reply('モバイル端末からパスワードをリセットすることはできません。PC版のメニューからどうぞ。')


@respond_to(r'^sl(\s.*)?')
def lsReply(message, *args):
    message.reply(':train:≡3')
    message.react('電車')


@respond_to(r'(.*)(疲れた|つかれた)(.*)')
def giveYouFireSpaghetti(message, *args):
    body = message.body['text']
    if args[0] == '':
        message.reply('なんだと？')
    else:
        message.reply(args[0] + 'だと？')
    message.reply('ったく……これ持って行けよ\n' + fire_spaghetti + '\n')
    message.reply('ファイヤースパゲティだ')
    message.reply('ただの燃えてるスパゲティだが、ないよりはマシだろう')

@respond_to(r'(.*)(ほめて|褒めて)(.*)')
def giveYouRingIine(message, *args):
    body = message.body['text']
    message.reply('おめでとう！お祝いのリングイーネだっ！\n' + ring_Iine)
