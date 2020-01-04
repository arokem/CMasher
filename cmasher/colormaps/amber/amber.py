from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.70219205e-04, 1.92123479e-04, 2.05867220e-04],
           [9.63039776e-04, 6.57034537e-04, 7.11879806e-04],
           [2.04508353e-03, 1.34366420e-03, 1.47063126e-03],
           [3.50855673e-03, 2.22748639e-03, 2.46041009e-03],
           [5.35221178e-03, 3.29213811e-03, 3.66701417e-03],
           [7.57776175e-03, 4.52536193e-03, 5.07987984e-03],
           [1.01885627e-02, 5.91736777e-03, 6.69055030e-03],
           [1.31889988e-02, 7.46000625e-03, 8.49191470e-03],
           [1.65841522e-02, 9.14629388e-03, 1.04777767e-02],
           [2.03796096e-02, 1.09701158e-02, 1.26425869e-02],
           [2.45813401e-02, 1.29260276e-02, 1.49812668e-02],
           [2.91956140e-02, 1.50091175e-02, 1.74890855e-02],
           [3.42289477e-02, 1.72149055e-02, 2.01615719e-02],
           [3.96880632e-02, 1.95392696e-02, 2.29944488e-02],
           [4.53186823e-02, 2.19783880e-02, 2.59835825e-02],
           [5.09056612e-02, 2.45286952e-02, 2.91249439e-02],
           [5.64622028e-02, 2.71868468e-02, 3.24145770e-02],
           [6.19922688e-02, 2.99496912e-02, 3.58485740e-02],
           [6.74993033e-02, 3.28142463e-02, 3.94230543e-02],
           [7.29863217e-02, 3.57776815e-02, 4.30396878e-02],
           [7.84559822e-02, 3.88373016e-02, 4.65895527e-02],
           [8.39107941e-02, 4.19480501e-02, 5.00844940e-02],
           [8.93527215e-02, 4.50014516e-02, 5.35265159e-02],
           [9.47836413e-02, 4.80080968e-02, 5.69173388e-02],
           [1.00205242e-01, 5.09701470e-02, 6.02584676e-02],
           [1.05619220e-01, 5.38894668e-02, 6.35511599e-02],
           [1.11026840e-01, 5.67679342e-02, 6.67966009e-02],
           [1.16429304e-01, 5.96072443e-02, 6.99958111e-02],
           [1.21827917e-01, 6.24088295e-02, 7.31496016e-02],
           [1.27223660e-01, 6.51741511e-02, 7.62587461e-02],
           [1.32617373e-01, 6.79046058e-02, 7.93239368e-02],
           [1.38010234e-01, 7.06012303e-02, 8.23456011e-02],
           [1.43402730e-01, 7.32653853e-02, 8.53243319e-02],
           [1.48795825e-01, 7.58980074e-02, 8.82604179e-02],
           [1.54190047e-01, 7.85002163e-02, 9.11542354e-02],
           [1.59586140e-01, 8.10728975e-02, 9.40059742e-02],
           [1.64984550e-01, 8.36170507e-02, 9.68158769e-02],
           [1.70385967e-01, 8.61334374e-02, 9.95839910e-02],
           [1.75790639e-01, 8.86230463e-02, 1.02310507e-01],
           [1.81199308e-01, 9.10864693e-02, 1.04995296e-01],
           [1.86612115e-01, 9.35246483e-02, 1.07638472e-01],
           [1.92029472e-01, 9.59382903e-02, 1.10239952e-01],
           [1.97451875e-01, 9.83279946e-02, 1.12799541e-01],
           [2.02879425e-01, 1.00694589e-01, 1.15317210e-01],
           [2.08312404e-01, 1.03038737e-01, 1.17792780e-01],
           [2.13751162e-01, 1.05361019e-01, 1.20225975e-01],
           [2.19195868e-01, 1.07662104e-01, 1.22616579e-01],
           [2.24646639e-01, 1.09942672e-01, 1.24964368e-01],
           [2.30103634e-01, 1.12203343e-01, 1.27269042e-01],
           [2.35566986e-01, 1.14444731e-01, 1.29530282e-01],
           [2.41036796e-01, 1.16667448e-01, 1.31747740e-01],
           [2.46513142e-01, 1.18872102e-01, 1.33921051e-01],
           [2.51996072e-01, 1.21059305e-01, 1.36049828e-01],
           [2.57485608e-01, 1.23229667e-01, 1.38133666e-01],
           [2.62981743e-01, 1.25383805e-01, 1.40172143e-01],
           [2.68484448e-01, 1.27522341e-01, 1.42164823e-01],
           [2.73993663e-01, 1.29645902e-01, 1.44111256e-01],
           [2.79509303e-01, 1.31755126e-01, 1.46010978e-01],
           [2.85031258e-01, 1.33850661e-01, 1.47863518e-01],
           [2.90559389e-01, 1.35933165e-01, 1.49668394e-01],
           [2.96093532e-01, 1.38003309e-01, 1.51425117e-01],
           [3.01633598e-01, 1.40061700e-01, 1.53133095e-01],
           [3.07179344e-01, 1.42109059e-01, 1.54791846e-01],
           [3.12730463e-01, 1.44146149e-01, 1.56400926e-01],
           [3.18286742e-01, 1.46173661e-01, 1.57959772e-01],
           [3.23847994e-01, 1.48192261e-01, 1.59467758e-01],
           [3.29413733e-01, 1.50202847e-01, 1.60924547e-01],
           [3.34983797e-01, 1.52206062e-01, 1.62329427e-01],
           [3.40557687e-01, 1.54202814e-01, 1.63682030e-01],
           [3.46135105e-01, 1.56193856e-01, 1.64981737e-01],
           [3.51715546e-01, 1.58180101e-01, 1.66228145e-01],
           [3.57298674e-01, 1.60162334e-01, 1.67420623e-01],
           [3.62883858e-01, 1.62141575e-01, 1.68558882e-01],
           [3.68470770e-01, 1.64118606e-01, 1.69642230e-01],
           [3.74058752e-01, 1.66094474e-01, 1.70670376e-01],
           [3.79647225e-01, 1.68070170e-01, 1.71642912e-01],
           [3.85235679e-01, 1.70046631e-01, 1.72559319e-01],
           [3.90823465e-01, 1.72024909e-01, 1.73419245e-01],
           [3.96409886e-01, 1.74006100e-01, 1.74222404e-01],
           [4.01994265e-01, 1.75991288e-01, 1.74968466e-01],
           [4.07575893e-01, 1.77981586e-01, 1.75657139e-01],
           [4.13154027e-01, 1.79978136e-01, 1.76288173e-01],
           [4.18727896e-01, 1.81982111e-01, 1.76861360e-01],
           [4.24296695e-01, 1.83994710e-01, 1.77376540e-01],
           [4.29859590e-01, 1.86017160e-01, 1.77833604e-01],
           [4.35415718e-01, 1.88050710e-01, 1.78232495e-01],
           [4.40964190e-01, 1.90096636e-01, 1.78573214e-01],
           [4.46504087e-01, 1.92156233e-01, 1.78855817e-01],
           [4.52034468e-01, 1.94230815e-01, 1.79080426e-01],
           [4.57554367e-01, 1.96321712e-01, 1.79247225e-01],
           [4.63062800e-01, 1.98430270e-01, 1.79356464e-01],
           [4.68558776e-01, 2.00557827e-01, 1.79408427e-01],
           [4.74041300e-01, 2.02705725e-01, 1.79403437e-01],
           [4.79509291e-01, 2.04875362e-01, 1.79342054e-01],
           [4.84961699e-01, 2.07068104e-01, 1.79224814e-01],
           [4.90397508e-01, 2.09285273e-01, 1.79052216e-01],
           [4.95815623e-01, 2.11528247e-01, 1.78825017e-01],
           [5.01214955e-01, 2.13798375e-01, 1.78544027e-01],
           [5.06594485e-01, 2.16096939e-01, 1.78209944e-01],
           [5.11953092e-01, 2.18425275e-01, 1.77823821e-01],
           [5.17289735e-01, 2.20784640e-01, 1.77386596e-01],
           [5.22603357e-01, 2.23176273e-01, 1.76899335e-01],
           [5.27892901e-01, 2.25601390e-01, 1.76363229e-01],
           [5.33157362e-01, 2.28061136e-01, 1.75779430e-01],
           [5.38395706e-01, 2.30556648e-01, 1.75149304e-01],
           [5.43606972e-01, 2.33088975e-01, 1.74474132e-01],
           [5.48790181e-01, 2.35659144e-01, 1.73755403e-01],
           [5.53944418e-01, 2.38268100e-01, 1.72994542e-01],
           [5.59068775e-01, 2.40916741e-01, 1.72193127e-01],
           [5.64162400e-01, 2.43605891e-01, 1.71352717e-01],
           [5.69224466e-01, 2.46336311e-01, 1.70474959e-01],
           [5.74254192e-01, 2.49108690e-01, 1.69561526e-01],
           [5.79250842e-01, 2.51923645e-01, 1.68614118e-01],
           [5.84213718e-01, 2.54781720e-01, 1.67634497e-01],
           [5.89142181e-01, 2.57683384e-01, 1.66624400e-01],
           [5.94035624e-01, 2.60629036e-01, 1.65585653e-01],
           [5.98893507e-01, 2.63618991e-01, 1.64520006e-01],
           [6.03715319e-01, 2.66653504e-01, 1.63429343e-01],
           [6.08500622e-01, 2.69732743e-01, 1.62315383e-01],
           [6.13249000e-01, 2.72856821e-01, 1.61180087e-01],
           [6.17960119e-01, 2.76025767e-01, 1.60025116e-01],
           [6.22633662e-01, 2.79239557e-01, 1.58852422e-01],
           [6.27269383e-01, 2.82498095e-01, 1.57663720e-01],
           [6.31867075e-01, 2.85801229e-01, 1.56460779e-01],
           [6.36426565e-01, 2.89148750e-01, 1.55245529e-01],
           [6.40947745e-01, 2.92540394e-01, 1.54019559e-01],
           [6.45430534e-01, 2.95975851e-01, 1.52784628e-01],
           [6.49874890e-01, 2.99454756e-01, 1.51542651e-01],
           [6.54280820e-01, 3.02976715e-01, 1.50295150e-01],
           [6.58648358e-01, 3.06541290e-01, 1.49043823e-01],
           [6.62977573e-01, 3.10148008e-01, 1.47790349e-01],
           [6.67268569e-01, 3.13796359e-01, 1.46536485e-01],
           [6.71521475e-01, 3.17485815e-01, 1.45283828e-01],
           [6.75736450e-01, 3.21215828e-01, 1.44033953e-01],
           [6.79913675e-01, 3.24985822e-01, 1.42788476e-01],
           [6.84053355e-01, 3.28795211e-01, 1.41549000e-01],
           [6.88155717e-01, 3.32643390e-01, 1.40317119e-01],
           [6.92221002e-01, 3.36529747e-01, 1.39094415e-01],
           [6.96249473e-01, 3.40453663e-01, 1.37882462e-01],
           [7.00241403e-01, 3.44414515e-01, 1.36682828e-01],
           [7.04197077e-01, 3.48411676e-01, 1.35497078e-01],
           [7.08116802e-01, 3.52444511e-01, 1.34326855e-01],
           [7.12000897e-01, 3.56512381e-01, 1.33173827e-01],
           [7.15849660e-01, 3.60614686e-01, 1.32039427e-01],
           [7.19663407e-01, 3.64750819e-01, 1.30925224e-01],
           [7.23442473e-01, 3.68920160e-01, 1.29832894e-01],
           [7.27187230e-01, 3.73122062e-01, 1.28764310e-01],
           [7.30897952e-01, 3.77356004e-01, 1.27720734e-01],
           [7.34575012e-01, 3.81621360e-01, 1.26704056e-01],
           [7.38218757e-01, 3.85917553e-01, 1.25715994e-01],
           [7.41829481e-01, 3.90244070e-01, 1.24758016e-01],
           [7.45407596e-01, 3.94600286e-01, 1.23832229e-01],
           [7.48953361e-01, 3.98985748e-01, 1.22939978e-01],
           [7.52467174e-01, 4.03399870e-01, 1.22083332e-01],
           [7.55949344e-01, 4.07842171e-01, 1.21263951e-01],
           [7.59400150e-01, 4.12312207e-01, 1.20483415e-01],
           [7.62820059e-01, 4.16809362e-01, 1.19744128e-01],
           [7.66209272e-01, 4.21333289e-01, 1.19047394e-01],
           [7.69568114e-01, 4.25883533e-01, 1.18395079e-01],
           [7.72896945e-01, 4.30459614e-01, 1.17789192e-01],
           [7.76196111e-01, 4.35061076e-01, 1.17231688e-01],
           [7.79465857e-01, 4.39687570e-01, 1.16724170e-01],
           [7.82706491e-01, 4.44338693e-01, 1.16268489e-01],
           [7.85918318e-01, 4.49014059e-01, 1.15866475e-01],
           [7.89101634e-01, 4.53713293e-01, 1.15519931e-01],
           [7.92256732e-01, 4.58436039e-01, 1.15230627e-01],
           [7.95383896e-01, 4.63181950e-01, 1.15000292e-01],
           [7.98483406e-01, 4.67950698e-01, 1.14830608e-01],
           [8.01555533e-01, 4.72741967e-01, 1.14723202e-01],
           [8.04600542e-01, 4.77555453e-01, 1.14679641e-01],
           [8.07618691e-01, 4.82390869e-01, 1.14701419e-01],
           [8.10610230e-01, 4.87247939e-01, 1.14789959e-01],
           [8.13575401e-01, 4.92126401e-01, 1.14946597e-01],
           [8.16514512e-01, 4.97025949e-01, 1.15172754e-01],
           [8.19427837e-01, 5.01946311e-01, 1.15469677e-01],
           [8.22315509e-01, 5.06887333e-01, 1.15838206e-01],
           [8.25177740e-01, 5.11848803e-01, 1.16279292e-01],
           [8.28014898e-01, 5.16830398e-01, 1.16794109e-01],
           [8.30827169e-01, 5.21831938e-01, 1.17383338e-01],
           [8.33614631e-01, 5.26853334e-01, 1.18047351e-01],
           [8.36377730e-01, 5.31894223e-01, 1.18787147e-01],
           [8.39116524e-01, 5.36954540e-01, 1.19602848e-01],
           [8.41831212e-01, 5.42034118e-01, 1.20494761e-01],
           [8.44522158e-01, 5.47132677e-01, 1.21463361e-01],
           [8.47189320e-01, 5.52250237e-01, 1.22508317e-01],
           [8.49833189e-01, 5.57386438e-01, 1.23630093e-01],
           [8.52453669e-01, 5.62541344e-01, 1.24828091e-01],
           [8.55051183e-01, 5.67714660e-01, 1.26102435e-01],
           [8.57625792e-01, 5.72906344e-01, 1.27452601e-01],
           [8.60177620e-01, 5.78116318e-01, 1.28878084e-01],
           [8.62707127e-01, 5.83344278e-01, 1.30378745e-01],
           [8.65214151e-01, 5.88590347e-01, 1.31953533e-01],
           [8.67699024e-01, 5.93854318e-01, 1.33601985e-01],
           [8.70162049e-01, 5.99136010e-01, 1.35323508e-01],
           [8.72603152e-01, 6.04435495e-01, 1.37117005e-01],
           [8.75022517e-01, 6.09752675e-01, 1.38981646e-01],
           [8.77420560e-01, 6.15087311e-01, 1.40916786e-01],
           [8.79797284e-01, 6.20439435e-01, 1.42921290e-01],
           [8.82152781e-01, 6.25809020e-01, 1.44994099e-01],
           [8.84487220e-01, 6.31195997e-01, 1.47134203e-01],
           [8.86800766e-01, 6.36600300e-01, 1.49340565e-01],
           [8.89093640e-01, 6.42021836e-01, 1.51612170e-01],
           [8.91366051e-01, 6.47460522e-01, 1.53947970e-01],
           [8.93618018e-01, 6.52916394e-01, 1.56346759e-01],
           [8.95849690e-01, 6.58389412e-01, 1.58807435e-01],
           [8.98061211e-01, 6.63879541e-01, 1.61328894e-01],
           [9.00252723e-01, 6.69386751e-01, 1.63910031e-01],
           [9.02424362e-01, 6.74911019e-01, 1.66549744e-01],
           [9.04576262e-01, 6.80452327e-01, 1.69246937e-01],
           [9.06708551e-01, 6.86010661e-01, 1.72000526e-01],
           [9.08821353e-01, 6.91586014e-01, 1.74809439e-01],
           [9.10914789e-01, 6.97178383e-01, 1.77672616e-01],
           [9.12988974e-01, 7.02787770e-01, 1.80589017e-01],
           [9.15044019e-01, 7.08414184e-01, 1.83557618e-01],
           [9.17080031e-01, 7.14057637e-01, 1.86577418e-01],
           [9.19097217e-01, 7.19718089e-01, 1.89647476e-01],
           [9.21095722e-01, 7.25395538e-01, 1.92766846e-01],
           [9.23075522e-01, 7.31090077e-01, 1.95934538e-01],
           [9.25036707e-01, 7.36801736e-01, 1.99149639e-01],
           [9.26979360e-01, 7.42530552e-01, 2.02411260e-01],
           [9.28903557e-01, 7.48276568e-01, 2.05718533e-01],
           [9.30809625e-01, 7.54039699e-01, 2.09070692e-01],
           [9.32697602e-01, 7.59820013e-01, 2.12466898e-01],
           [9.34567369e-01, 7.65617662e-01, 2.15906305e-01],
           [9.36418985e-01, 7.71432704e-01, 2.19388145e-01],
           [9.38252815e-01, 7.77265047e-01, 2.22911744e-01],
           [9.40068905e-01, 7.83114764e-01, 2.26476369e-01],
           [9.41867027e-01, 7.88982063e-01, 2.30081261e-01],
           [9.43647372e-01, 7.94866946e-01, 2.33725776e-01],
           [9.45410404e-01, 8.00769287e-01, 2.37409327e-01],
           [9.47155602e-01, 8.06689439e-01, 2.41131186e-01],
           [9.48883260e-01, 8.12627361e-01, 2.44890787e-01],
           [9.50593708e-01, 8.18583001e-01, 2.48687573e-01],
           [9.52286404e-01, 8.24556720e-01, 2.52520905e-01],
           [9.53962043e-01, 8.30548296e-01, 2.56390308e-01],
           [9.55620227e-01, 8.36558026e-01, 2.60295207e-01],
           [9.57261035e-01, 8.42585982e-01, 2.64235099e-01],
           [9.58884834e-01, 8.48632103e-01, 2.68209516e-01],
           [9.60491021e-01, 8.54696780e-01, 2.72217942e-01],
           [9.62080512e-01, 8.60779708e-01, 2.76259973e-01],
           [9.63652252e-01, 8.66881479e-01, 2.80335115e-01],
           [9.65207457e-01, 8.73001664e-01, 2.84442994e-01],
           [9.66744863e-01, 8.79140943e-01, 2.88583160e-01],
           [9.68265762e-01, 8.85298862e-01, 2.92755253e-01],
           [9.69768911e-01, 8.91476088e-01, 2.96958874e-01],
           [9.71255417e-01, 8.97672258e-01, 3.01193672e-01],
           [9.72724330e-01, 9.03887907e-01, 3.05459294e-01],
           [9.74176300e-01, 9.10122875e-01, 3.09755404e-01],
           [9.75610944e-01, 9.16377452e-01, 3.14081683e-01],
           [9.77028174e-01, 9.22651799e-01, 3.18437827e-01],
           [9.78428460e-01, 9.28945845e-01, 3.22823525e-01],
           [9.79810960e-01, 9.35260068e-01, 3.27238519e-01],
           [9.81176459e-01, 9.41594269e-01, 3.31682509e-01],
           [9.82524379e-01, 9.47948818e-01, 3.36155254e-01],
           [9.83854395e-01, 9.54323974e-01, 3.40656523e-01]]

test_cm = ListedColormap(cm_data, name="amber")
