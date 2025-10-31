<template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-last-column-table"
      flat
      bordered
      title="Employee Information"
      :rows="rows"
      :columns="columns"
      row-key="name"
    >
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn dense icon="mode_edit" @click="onEdit(props.row)"></q-btn>
          <q-btn dense icon="delete" @click="onDelete(props.row)"></q-btn>
        </q-td>
      </template>
    </q-table>
  </div>


<div>
      <q-dialog v-model="deleteData" persistent>
        <q-card>
          <q-card-section class="row items-center">
            <span class="q-ml-sm">Employee Deleted Successfully !!</span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="Ok" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>





  <div class="q-pa-md q-gutter-sm">
    <q-dialog v-model="confirm" persistent>
      <q-card flat bordered class="my-card">
        <q-card-section class="row items-center">
          <div class="text-h6">Update Employee Information</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input
            outlined
            v-model="updateInfo.name"
            @change="UpdateData(updateInfo)"
            type="text"
            label="Enter New Name"
          />
        </q-card-section>

        <q-separator inset />

        <q-card-section>
          <q-input
            outlined
            v-model="updateInfo.email"
            @change="UpdateData(updateInfo)"
            type="email"
            label="Enter New Email"
          />
        </q-card-section>

        <q-separator inset />
        <q-card-section>
          <q-select
            standout="bg-teal text-white"
            v-model="updateInfo.des"
            @change="UpdateData(updateInfo)"
            :options="options"
            label="Select Designation"
          />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" @click="cancelUpdate()" color="primary" v-close-popup />
          <q-btn
            flat
            label="Update Information"
            @click="confirmUpdate()"
            color="primary"
            v-close-popup
          />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <div>
      <q-dialog v-model="update" persistent>
        <q-card>
          <q-card-section class="row items-center">
            <span class="q-ml-sm">Employee Data Updated Successfully !!</span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="Ok" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </div>

  <div>
    <q-btn color="primary" @click="addNewEmp()" class="on-right" label="Add New Employee" />

    <q-dialog v-model="newEmp" persistent>
      <q-card flat bordered class="my-card">
        <q-card-section class="row items-center">
          <div class="text-h6">Add New Employee</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input outlined v-model="newEmpInfo.id" type="text" label="Enter New ID" />
        </q-card-section>

        <q-separator inset />
        <q-card-section class="q-pt-none">
          <q-input outlined v-model="newEmpInfo.name" type="text" label="Enter New Name" />
        </q-card-section>

        <q-separator inset />

        <q-card-section>
          <q-input outlined v-model="newEmpInfo.email" type="email" label="Enter New Email" />
        </q-card-section>
        <q-separator inset />
        <q-card-section>
          <q-select
            standout="bg-teal text-white"
            v-model="newEmpInfo.des"
            :options="options"
            label="Select Designation"
          />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" @click="cancelNew()" color="primary" v-close-popup />
          <q-btn flat label="Add New" @click="confirmAdd()" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <div>
      <q-dialog v-model="successfullyAdd" persistent>
        <q-card>
          <q-card-section class="row items-center">
            <span class="q-ml-sm">New Employee Added Successfully !!</span>
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="Ok" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    return {
      successfullyAdd: ref(false),
      deleteData : ref(false),
      options: ['Web Developer', 'Manager', 'HR', 'Business Analyst', 'Quality Assurance Engineer'],
      updateInfo: ref({
        name: '',
        email: '',
        des: null,
      }),

      tempInfo: ref({
        name: '',
        email: '',
        des: null,
      }),

      newEmp: ref(false),
      newEmpInfo: ref({
        id: '',
        name: '',
        email: '',
        des: null,
      }),

      confirmnewEmp: ref(false),

      confirm: ref(false),
      update: ref(false),
      columns: [
        { name: 'id', required: true, label: 'ID', align: 'left', field: 'id' },
        { name: 'name', required: true, label: 'Name', align: 'left', field: 'name' },
        { name: 'email', required: true, label: 'Email', align: 'left', field: 'email' },
        { name: 'des', required: true, label: 'Designation', align: 'left', field: 'des' },
        { name: 'actions', label: 'Action', align: 'left' },
      ],
      rows: ref([
        { id: 1, name: 'john', email: 'john@gmail.com', des: 'Developer' },
        { id: 2, name: 'tom', email: 'tom@gmail.com', des: 'Web Developer' },
        { id: 3, name: 'sam', email: 'sam@gmail.com', des: 'HR' },
      ]),
    }
  },

  methods: {
    addNewEmp() {
      this.newEmp = true
      this.newEmpInfo.id = ''
      this.newEmpInfo.name = ''
      this.newEmpInfo.email = ''
      this.newEmpInfo.des = null
    },

    confirmAdd() {
      this.rows.push({ ...this.newEmpInfo })
      this.successfullyAdd = true
    },

    cancelNew() {
      this.newEmpInfo.id = ''
      this.newEmpInfo.name = ''
      this.newEmpInfo.email = ''
      this.newEmpInfo.des = null
    },
    cancelUpdate() {
      this.update = false
    },

    confirmUpdate() {
      this.update = true

      this.rows = this.rows.map((emp) => {
        if (emp.name == this.tempInfo.name && emp.email == this.tempInfo.email) {
          emp.name = this.updateInfo.name
          emp.email = this.updateInfo.email
          emp.des = this.updateInfo.des
        }
        return emp
      })
    },

    UpdateData(row) {
      this.updateInfo.name = row.name
      this.updateInfo.email = row.email
      this.updateInfo.des = row.des
    },

    onEdit(row) {
      this.confirm = true
      this.updateInfo.name = row.name
      this.updateInfo.email = row.email
      this.updateInfo.des = row.des

      this.tempInfo.name = row.name
      this.tempInfo.email = row.email
    },

    onDelete(row) {
      this.deleteData = true
      this.rows = this.rows.filter((emp) => emp.id != row.id)
    },
  },
}
</script>
