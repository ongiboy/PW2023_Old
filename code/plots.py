import matplotlib.pyplot as plt

run_pre = "FD_AB_p"
run_fine = ""

jobs_pre = {"FD_AB_p": "Run_16839155",
            "": ""}
jobs_fine = {
             "": ""}




#### PRETRAINING ####
job_pre = jobs_pre[run_pre]
if job_pre == "":
    pass
elif job_pre == "Run_16839155":
    loss = [1.0476127862930298, -1.08078932762146, -1.8135979175567627, -2.430058717727661, -2.752322196960449, -3.0237550735473633, -3.1621780395507812, -3.254225254058838, -3.323082208633423, -3.5701518058776855, -3.5892012119293213, -3.578486919403076, -3.7899749279022217, -3.9621291160583496, -3.855351686477661, -3.8915815353393555, -4.063992500305176, -4.088557243347168, -4.074591636657715, -4.155910491943359, -4.2325968742370605, -4.438491344451904, -4.434119701385498, -4.531982421875, -4.6677680015563965, -5.056972503662109, -5.247226238250732, -5.250253677368164, -5.147713661193848, -5.469674587249756, -5.5761399269104, -5.626694202423096, -5.653103351593018, -5.611390590667725, -5.76519250869751, -5.885776519775391, -5.950704574584961, -5.860759258270264, -5.886518955230713, -5.94200325012207]

### FINE TUNING ###
job_fine = jobs_fine[run_fine]
if job_fine == "":
    pass
elif job_fine == "":
    1



#### PLOTTING PRE TRAINING ####
if run_pre != "" and False:
    # Plot data on each subplot
    fig, axs = plt.subplots(2, 3, figsize=(8, 5))
    axs[0, 0].plot(loss)
    axs[0, 1].plot(loss_t)
    axs[1, 0].plot(loss_f)
    axs[1, 1].plot(loss_c)
    axs[1, 2].plot(loss_TF)

    axs[0, 0].set_title('Average loss')
    axs[0, 1].set_title('Average loss time')
    axs[1, 0].set_title('Average loss frequency')
    axs[1, 1].set_title('Average loss c')
    axs[1, 2].set_title('Average loss TF')

    plt.tight_layout()
    plt.suptitle(f"Pre-training, {run_pre}")
    plt.subplots_adjust(top=0.88)
    plt.show()
else:
    plt.plot(loss)
    plt.show()

##### PLOTTING FINE TUNE #####
if run_fine != "":
    fig, axs = plt.subplots(2, 2, figsize=(7, 6))
    axs[0, 0].plot(Finetune_Accuracies)
    axs[0, 1].plot(Finetune_Losses)
    axs[1, 0].plot(Test_Accuracies)
    axs[1, 1].plot(Test_Losses)

    axs[0, 0].set_title('Finetune accuracy')
    axs[0, 1].set_title('Finetune loss')
    axs[1, 0].set_title('Test accuracy')
    axs[1, 1].set_title('Test loss')

    plt.tight_layout()
    plt.suptitle(f"Fine-tuning, {run_fine}")
    plt.subplots_adjust(top=0.88)
    plt.show()