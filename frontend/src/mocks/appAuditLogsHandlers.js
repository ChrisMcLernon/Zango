import { faker } from '@faker-js/faker';
import { rest } from 'msw';

const range = (len) => {
	const arr = [];
	for (let i = 0; i < len; i++) {
		arr.push(i);
	}
	return arr;
};

const newApp = () => {
	return {
		id: faker.number.int(1000),
		schema_name: faker.internet.displayName(),
		created_at: faker.date.past(),
		created_by: faker.person.fullName(),
		modified_at: faker.date.past(),
		modified_by: faker.person.fullName(),
		uuid: faker.number.int({ min: 1000, max: 9999 }),
		name: 'App ' + faker.number.int({ min: 1, max: 10 }),
		description: faker.lorem.sentences(2),
		tenant_type: 'app',
		is_active: faker.datatype.boolean(),
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
	};
};

const newRole = () => {
	return {
		id: faker.number.int(1000),
		schema_name: faker.internet.displayName(),
		created_at: faker.date.past(),
		created_by: faker.person.fullName(),
		modified_at: faker.date.past(),
		modified_by: faker.person.fullName(),
		uuid: faker.number.int({ min: 1000, max: 9999 }),
		name: 'Role ' + faker.number.int({ min: 1, max: 10 }),
		description: faker.lorem.sentences(2),
		tenant_type: 'role',
		is_active: faker.datatype.boolean(),
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
	};
};

const newPolicy = () => {
	return {
		id: faker.number.int(1000),
		schema_name: faker.internet.displayName(),
		created_at: faker.date.past(),
		created_by: faker.person.fullName(),
		modified_at: faker.date.past(),
		modified_by: faker.person.fullName(),
		uuid: faker.number.int({ min: 1000, max: 9999 }),
		name: 'Policy ' + faker.number.int({ min: 1, max: 10 }),
		description: faker.lorem.sentences(2),
		tenant_type: 'policy',
		is_active: faker.datatype.boolean(),
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
	};
};

const newUser = () => {
	return {
		id: faker.number.int({ min: 1000, max: 9999 }),
		actor: null,
		action: 'Update',
		object: 'Role2',
		object_id: 2,
		object_uuid: '3f89a5ab-5f5c-49de-9d57-85d6793805aa',
		object_type: 'asd asd asd asd',
		timestamp: faker.date.past(),
		// changes: {
		// 	id: ['None', '5'],
		// 	name: ['None', 'Role3'],
		// 	is_active: ['None', 'False'],
		// 	created_at: ['None', faker.date.past()],
		// 	created_by: ['None', ''],
		// 	is_default: [
		// 		'None',
		// 		'https://www.figma.com/file/loWIKpXsRPcH7U4SBeuKNY/Icons?type=design&node-id=1489-32&mode=design&t=KqFQ1TyYXRsf6kaa-0',
		// 	],
		// 	modified_at: ['None', faker.date.past()],
		// 	modified_by: ['None', ''],
		// 	id1: ['None', '5'],
		// 	name1: ['None', 'Role3'],
		// 	is_active1: ['None', 'False'],
		// 	created_at1: ['None', faker.date.past()],
		// 	created_by1: ['None', ''],
		// 	is_default1: [
		// 		'None',
		// 		'https://www.figma.com/file/loWIKpXsRPcH7U4SBeuKNY/Icons?type=design&node-id=1489-32&mode=design&t=KqFQ1TyYXRsf6kaa-0',
		// 	],
		// 	modified_at1: ['None', faker.date.past()],
		// 	modified_by1: ['None', ''],
		// 	id12: ['None', '5'],
		// 	name12: ['None', 'Role3'],
		// 	is_active12: ['None', 'False'],
		// 	created_at12: ['None', faker.date.past()],
		// 	created_by12: ['None', ''],
		// 	is_default12: [
		// 		'None',
		// 		'https://www.figma.com/file/loWIKpXsRPcH7U4SBeuKNY/Icons?type=design&node-id=1489-32&mode=design&t=KqFQ1TyYXRsf6kaa-0',
		// 	],
		// 	modified_at12: ['None', faker.date.past()],
		// 	modified_by12: ['None', ''],
		// 	id123: ['None', '5'],
		// 	name123: ['None', 'Role3'],
		// 	is_active123: ['None', 'False'],
		// 	created_at123: ['None', faker.date.past()],
		// 	created_by123: ['None', ''],
		// 	is_default123: [
		// 		'None',
		// 		'https://www.figma.com/file/loWIKpXsRPcH7U4SBeuKNY/Icons?type=design&node-id=1489-32&mode=design&t=KqFQ1TyYXRsf6kaa-0',
		// 	],
		// 	modified_at123: ['None', faker.date.past()],
		// 	modified_by123: ['None', ''],
		// },
		// changes: {
		// 	policies: {
		// 		type: 'm2m',
		// 		objects: ['FrameRouterViewAccess'],
		// 		operation: 'add',
		// 	},
		// },
		changes: {
			config: [
				'{"background_color": "#5048ED", "card_color": "#5048ED", "card_title": "", "corner_radius": 4, "header_text": "", "logo_placement": "topLeft", "paragraph_text": ""}',
				'{"background_color": "#5048ED", "card_color": "#5048ED", "card_title": "", "corner_radius": 4, "header_text": "LoginTexts", "logo_placement": "topLeft", "paragraph_text": ""}',
			],
			is_active: ['None', 'False'],
			created_at: ['None', faker.date.past()],
		},
	};
};

export function makeRoles(...lens) {
	const makeDataLevel = (depth = 0) => {
		const len = lens[depth];
		return range(len).map((d) => {
			return {
				...newRole(),
				subRows: lens[depth + 1] ? makeDataLevel(depth + 1) : undefined,
			};
		});
	};

	return makeDataLevel();
}

export function makePolicies(...lens) {
	const makeDataLevel = (depth = 0) => {
		const len = lens[depth];
		return range(len).map((d) => {
			return {
				...newPolicy(),
				subRows: lens[depth + 1] ? makeDataLevel(depth + 1) : undefined,
			};
		});
	};

	return makeDataLevel();
}

export function makeData(...lens) {
	const makeDataLevel = (depth = 0) => {
		const len = lens[depth];
		return range(len).map((d) => {
			return {
				...newUser(),
				subRows: lens[depth + 1] ? makeDataLevel(depth + 1) : undefined,
			};
		});
	};

	return makeDataLevel();
}

let totalData = 1000;
const data = makeData(totalData);

export const appAuditLogsHandlers = [
	rest.get('/api/v1/apps/:appId/auditlog/', (req, res, ctx) => {
		const pageIndex = parseInt(req.url.searchParams.get('page')) || 0;
		const pageSize = parseInt(req.url.searchParams.get('page_size')) || 10;
		const searchValue = req.url.searchParams.get('search') || '';
		let slicedData = data.slice(
			pageIndex * pageSize,
			(pageIndex + 1) * pageSize
		);

		return res(
			ctx.delay(500),
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					audit_logs: {
						total_records: totalData,
						total_pages: Math.ceil(data.length / pageSize),
						next: 'http://localhost:8000/api/v1/auth/platform-users/?page=2',
						previous: null,
						records: searchValue ? [] : slicedData,
					},
					dropdown_options: {
						action: [
							{
								id: '0',
								label: 'Create',
							},
							{
								id: '1',
								label: 'Update',
							},
							{
								id: '2',
								label: 'Delete',
							},
							{
								id: '3',
								label: 'Access',
							},
						],
						object_type: [
							{
								id: 58,
								label: 'spoccustomer',
							},
							{
								id: 50,
								label: 'spoc',
							},
							{
								id: 37,
								label: 'commmunicationactivemodel',
							},
							{
								id: 32,
								label: 'genericloginconfigmodel',
							},
							{
								id: 22,
								label: 'app user model',
							},
							{
								id: 21,
								label: 'user role model',
							},
						],
					},
					message: 'Platform user fetched successfully',
				},
			})
		);
	}),

	rest.post('/api/v1/apps/:appId/auditlog/', (req, res, ctx) => {
		return res(
			ctx.delay(500),
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					message: 'Platform user fetched successfully',
				},
			})
		);
	}),

	rest.put('/api/v1/apps/:appId/auditlog/:id', (req, res, ctx) => {
		return res(
			ctx.delay(500),
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					message: 'Platform user fetched successfully',
				},
			})
		);
	}),
];
